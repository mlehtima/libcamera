Name:       libcamera
Summary:    A library to support complex camera ISPs
Version:    0.0.3
Release:    1
License:    LGPLv2+
URL:        https://libcamera.org
Source:     %{name}-%{version}.tar.bz2
Patch0:     fallthrough.patch
Patch1:     gnutls2.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: meson
BuildRequires: ninja
BuildRequires: python3-jinja2
BuildRequires: python3-ply
BuildRequires: python3-yaml
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(yaml-0.1)

%description
libcamera is a library that deals with heavy hardware image processing
operations of complex camera devices that are shared between the linux
host all while allowing offload of certain aspects to the control of
complex camera hardware such as ISPs.

Hardware support includes USB UVC cameras, libv4l cameras as well as more
complex ISPs (Image Signal Processor).

%package devel
Summary: Development files for libcamera
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson \
    -Dcam=disabled \
    -Ddocumentation=disabled \
    -Dgstreamer=enabled \
    -Dlc-compliance=disabled \
    -Dqcam=disabled \
    -Dtracing=disabled \
    -Dv4l2=true

%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING.rst LICENSES/LGPL-2.1-or-later.txt
%{_bindir}/libcamerify
%{_datadir}/libcamera/
%{_libdir}/gstreamer-1.0/libgstlibcamera.so
%{_libdir}/libcamera/
%{_libdir}/libcamera*.so.*
%{_libdir}/v4l2-compat.so
%{_libexecdir}/libcamera/

%files devel
%{_includedir}/libcamera
%{_libdir}/libcamera*.so
%{_libdir}/pkgconfig/*.pc
